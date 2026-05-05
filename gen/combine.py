from __future__ import annotations

from pathlib import Path


SOURCE_DIR = Path(
	r"c:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\docs\sentences\categories"
)
OUTPUT_FILE = Path(
	r"c:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\gen\rawdata.txt"
)


def iter_text_files(source_dir: Path) -> list[Path]:
	return sorted(
		[
			path
			for path in source_dir.rglob("*.txt")
			if path.is_file() and path.resolve() != OUTPUT_FILE.resolve()
		]
	)


def combine_text_files(source_dir: Path, output_file: Path) -> int:
	text_files = iter_text_files(source_dir)
	output_file.parent.mkdir(parents=True, exist_ok=True)

	combined_lines = 0
	with output_file.open("w", encoding="utf-8", newline="\n") as output_handle:
		for text_file in text_files:
			with text_file.open("r", encoding="utf-8") as input_handle:
				for line in input_handle:
					output_handle.write(line)
					combined_lines += 1
			output_handle.write("\n")
			combined_lines += 1

	return combined_lines


def main() -> None:
	if not SOURCE_DIR.exists():
		raise FileNotFoundError(f"Source directory does not exist: {SOURCE_DIR}")

	total_lines = combine_text_files(SOURCE_DIR, OUTPUT_FILE)
	print(f"Combined {total_lines} lines into {OUTPUT_FILE}")


if __name__ == "__main__":
	main()
