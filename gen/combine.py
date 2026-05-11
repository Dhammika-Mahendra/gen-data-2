from __future__ import annotations

from pathlib import Path


# Hardcoded directory containing the source .txt files.
SOURCE_DIR = Path(
	r"C:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\gen\shuffle"
)
# Hardcoded destination file path.
DEST_FILE = Path(
	r"C:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\gen\rawdata.txt"
)


def main() -> None:
	if not SOURCE_DIR.exists():
		raise FileNotFoundError(f"Source directory not found: {SOURCE_DIR}")

	txt_files = sorted(path for path in SOURCE_DIR.glob("*.txt") if path.is_file())
	if not txt_files:
		raise FileNotFoundError(f"No .txt files found in: {SOURCE_DIR}")

	# Clear destination file first.
	DEST_FILE.write_text("", encoding="utf-8")

	with DEST_FILE.open("a", encoding="utf-8") as output:
		for path in txt_files:
			if path.resolve() == DEST_FILE.resolve():
				continue
			output.write(f"[{path.stem}]\n")
			content = path.read_text(encoding="utf-8")
			if content and not content.endswith("\n"):
				content += "\n"
			output.write(content)


if __name__ == "__main__":
	main()
