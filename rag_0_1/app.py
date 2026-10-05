from flask import Flask

from routes.rag_routes import rag_bp


def create_app():

    app = Flask(__name__)

    app.register_blueprint(rag_bp)

    return app


app = create_app()


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )





# CURL endpoint usage

# 1. ingest doc
#  curl.exe -X POST "http://localhost:5000/api/rag/documents" -F "file=@C:\Users\yuges\OneDrive\Desktop\rag_0_1\document_rag\data\documents\test_doc.pdf" -F "document_id=doc_001"

# 2. update doc
# curl.exe -X PUT "http://localhost:5000/api/rag/documents/doc_001" -F "file=@data/documents/updated.pdf"