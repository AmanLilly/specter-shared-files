from difflib import SequenceMatcher

def compare_sentences(sentence1: str, sentence2: str) -> dict:
    """
    Compare two sentences and return their similarity ratio and differences.
    
    Args:
        sentence1 (str): First sentence to compare
        sentence2 (str): Second sentence to compare
        
    Returns:
        dict: Dictionary containing similarity ratio and differences
    """
    # Create a SequenceMatcher object
    matcher = SequenceMatcher(None, sentence1, sentence2)
    
    # Get the similarity ratio
    similarity = matcher.ratio()
    
    # Get the differences
    differences = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'replace':
            differences.append(f"Replace '{sentence1[i1:i2]}' with '{sentence2[j1:j2]}'")
        elif tag == 'delete':
            differences.append(f"Delete '{sentence1[i1:i2]}'")
        elif tag == 'insert':
            differences.append(f"Insert '{sentence2[j1:j2]}'")
            
    return {
        'similarity_ratio': round(similarity * 100, 2),
        'differences': differences
    }

# Example usage
if __name__ == "__main__":
    sentence1 = "The quick brown fox jumps over the lazy dog"
    sentence2 = "The quick brown cat jumps over the sleeping dog"
    
    result = compare_sentences(sentence1, sentence2)
    print(f"Similarity: {result['similarity_ratio']}%")
    print("\nDifferences:")
    for diff in result['differences']:
        print(f"- {diff}")