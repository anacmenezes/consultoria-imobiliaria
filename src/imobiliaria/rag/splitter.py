
def split_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
):
    if chunk_size <= 0:
        raise ValueError("chunk_size deve ser maior que zero.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap deve ser >= 0 e menor que chunk_size.")

    words = text.split()
    chunks = []
    current_words = []
    current_length = 0

    for word in words:
        added_length = len(word) + (1 if current_words else 0)

        if current_words and current_length + added_length > chunk_size:
            chunks.append(" ".join(current_words))

            # Mantém palavras anteriores para criar a sobreposição.
            overlap_words = []
            overlap_length = 0

            for previous_word in reversed(current_words):
                extra = len(previous_word) + (1 if overlap_words else 0)

                if overlap_length + extra > overlap:
                    break

                overlap_words.insert(0, previous_word)
                overlap_length += extra

            current_words = overlap_words
            current_length = overlap_length

        if current_words:
            current_length += len(word) + 1
        else:
            current_length = len(word)

        current_words.append(word)

    if current_words:
        chunks.append(" ".join(current_words))

    return chunks