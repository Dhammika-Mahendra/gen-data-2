from pathlib import Path


def read_sentences(file_path: Path) -> list[str]:
	return file_path.read_text(encoding="utf-8").splitlines()


def interleave_halves(sentences: list[str]) -> list[str]:
	midpoint = (len(sentences) + 1) // 2
	first_half = sentences[:midpoint]
	second_half = sentences[midpoint:]

	merged: list[str] = []
	for index in range(max(len(first_half), len(second_half))):
		if index < len(first_half):
			merged.append(first_half[index])
		if index < len(second_half):
			merged.append(second_half[index])

	return merged


def main() -> None:
	# TODO: Replace with the exact input file you want to process.
	input_file = Path(r"C:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\docs\sentences\new categories\PUBLIC.txt")
	output_dir = Path(r"C:\Users\wmdha\Documents\UoM BSc IT\Lessons\L4S7\Reserach - Group project\Code\gen data 2\docs\sentences\new categories\merged")
	output_file = output_dir / f"{input_file.stem}_merged.txt"

	sentences = read_sentences(input_file)
	merged = interleave_halves(sentences)

	output_dir.mkdir(parents=True, exist_ok=True)
	output_file.write_text("\n".join(merged) + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()
