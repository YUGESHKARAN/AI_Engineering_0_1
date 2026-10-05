from flask import Blueprint, request, jsonify

from ingestion.ingest import ingest_document
from ingestion.document_manager import (
    delete_document,
    update_document
)

from retrieval.rag_chain import answer_question


rag_bp = Blueprint(
    "rag",
    __name__,
    url_prefix="/api/rag"
)

# Ingestion endpoint
@rag_bp.post("/documents")
def upload_document():

    if "file" not in request.files:
        return jsonify({
            "error": "No file provided"
        }), 400

    file = request.files["file"]

    document_id = request.form.get(
        "document_id"
    )

    if not document_id:
        return jsonify({
            "error": "document_id is required"
        }), 400

    if not file.filename:
        return jsonify({
            "error": "Invalid filename"
        }), 400

    file_path = (
        f"data/documents/{file.filename}"
    )

    file.save(file_path)

    try:

        result = ingest_document(
            file_path=file_path,
            document_id=document_id
        )

        return jsonify(result), 201

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500



# Query endpoint
@rag_bp.post("/query")
def query_document():

    data = request.get_json()

    question = data.get("question")
    document_id = data.get("document_id")

    if not question:
        return jsonify({
            "error": "question is required"
        }), 400

    if not document_id:
        return jsonify({
            "error": "document_id is required"
        }), 400

    try:

        result = answer_question(
            question=question,
            document_id=document_id
        )

        return jsonify(result)

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500


# Delete endpoint
@rag_bp.delete("/documents/<document_id>")
def delete_document_route(document_id):

    try:

        result = delete_document(
            document_id
        )

        return jsonify(result)

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500


# Update endpoint
@rag_bp.put("/documents/<document_id>")
def update_document_route(document_id):

    if "file" not in request.files:
        return jsonify({
            "error": "No file provided"
        }), 400

    file = request.files["file"]

    file_path = (
        f"data/documents/{file.filename}"
    )

    file.save(file_path)

    try:

        result = update_document(
            file_path=file_path,
            document_id=document_id
        )

        return jsonify(result)

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500