import tkinter as tk
from tkinter import filedialog, scrolledtext
from src.ingestion.loader import load_pdf_text
from src.ingestion.splitter import split_text
from src.embeddings.embedder import get_embedding_model
from src.embeddings.store import create_vectorstore
from src.retrieval.qa import build_qa_chain


class PDFQAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Document QA Agent")

        # Default PDF path
        self.pdf_path = "data/sample.pdf"

        # PDF Display
        self.label = tk.Label(root, text=f"Current PDF: {self.pdf_path}")
        self.label.pack(pady=5)

        # Browse Button
        self.browse_btn = tk.Button(root, text="Browse PDF", command=self.browse_file)
        self.browse_btn.pack(pady=5)

        # Prompt entry
        self.prompt_entry = tk.Entry(root, width=80)
        self.prompt_entry.pack(pady=10)

        # Submit button
        self.submit_btn = tk.Button(root, text="Ask", command=self.handle_question)
        self.submit_btn.pack(pady=5)

        # Output box
        self.output_box = scrolledtext.ScrolledText(root, width=100, height=20)
        self.output_box.pack(pady=10)

    def browse_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if filepath:
            self.pdf_path = filepath
            self.label.config(text=f"Current PDF: {self.pdf_path}")

    def handle_question(self):
        question = self.prompt_entry.get()
        self.output_box.insert(tk.END, f"> {question}\n")

        try:
            pages = load_pdf_text(self.pdf_path)
            chunks = split_text(pages, chunk_size=1000, overlap=200)
            model = get_embedding_model()
            vectorstore = create_vectorstore(chunks, model)
            qa_chain = build_qa_chain(vectorstore.as_retriever())
            response = qa_chain.invoke({"query": question})
            self.output_box.insert(tk.END, f"{response['result']}\n\n")
        except Exception as e:
            self.output_box.insert(tk.END, f"[ERROR] {e}\n\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFQAApp(root)
    root.mainloop()
