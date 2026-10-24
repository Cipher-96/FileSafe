import os
import shutil
import tempfile
from pathlib import Path
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {
    "doc", "docx", "ppt", "pptx", "xls", "xlsx",
    "pdf", "jpg", "jpeg", "png", "html"
}
MIME_TYPES = {
    "doc": "application/msword",
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "ppt": "application/vnd.ms-powerpoint",
    "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "xls": "application/vnd.ms-excel",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "pdf": "application/pdf",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "html": "text/html",
}

OFFICE_SOURCE_EXTS = {"doc", "docx", "ppt", "pptx", "xls", "xlsx"}
PDF_SOURCE_EXTS = {"pdf"}
IMAGE_SOURCE_EXTS = {"jpg", "jpeg", "png"}
FILESIZE_LIMIT = 100 * 1024 * 1024


def normalize_ext(value: str) -> str:
    return (value or "").strip().lower().lstrip(".")


def is_allowed_extension(ext: str) -> bool:
    return normalize_ext(ext) in ALLOWED_EXTENSIONS


def get_mime_for_extension(ext: str) -> str:
    return MIME_TYPES.get(normalize_ext(ext), "")


def safe_name(filename: str) -> str:
    base = secure_filename(filename)
    if not base:
        return "uploaded_file"
    return base


def make_temp_file_path(base_dir: str, original_name: str) -> str:
    base = safe_name(original_name)
    name, ext = os.path.splitext(base)
    fd, unique_path = tempfile.mkstemp(prefix=f"{name}-", suffix=ext, dir=base_dir)
    os.close(fd)
    return unique_path


def clear_temp_folder(base_path: str):
    if not base_path or not os.path.isdir(base_path):
        return
    for child in os.listdir(base_path):
        child_path = os.path.join(base_path, child)
        if os.path.isdir(child_path):
            shutil.rmtree(child_path, ignore_errors=True)
        else:
            try:
                os.remove(child_path)
            except OSError:
                pass


def ensure_secure_temp_dir(path: str) -> str:
    Path(path).mkdir(parents=True, exist_ok=True)
    return path


def is_valid_conversion(source_ext: str, target_ext: str) -> bool:
    source = normalize_ext(source_ext)
    target = normalize_ext(target_ext)
    if source in OFFICE_SOURCE_EXTS and target == "pdf":
        return True
    if source == "pdf" and target in {"doc", "docx", "ppt", "pptx", "xls", "xlsx"}:
        return True
    if source in IMAGE_SOURCE_EXTS and target == "pdf":
        return True
    if source == "pdf" and target in {"jpg", "png"}:
        return True
    if source == "html" and target == "pdf":
        return True
    if source == "pdf" and target == "html":
        return True
    return False
