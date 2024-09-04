def display_hangman(tries):
    stages = [
        """
    --------
    |      |
    |      
    |     
    |      
    |     
    ----|
    """,
        """
    --------
    |      |
    |      O
    |     
    |      
    |     
    ----|
    """,
        """
    --------
    |      |
    |      O
    |     /
    |      
    |     
    ----|
    """,
        """
    --------
    |      |
    |      O
    |     /|
    |      
    |     
    ----|
    """,
        """
    --------
    |      |
    |      O
    |     /|\\
    |      
    |    
    ----|
    """,
        """
    --------
    |      |
    |      O
    |     /|\\
    |      |
    |     
    ----|
    """,
        """
    --------
    |      |
    |      O
    |     /|\\
    |      |
    |     / 
    ----|
    """,
        """
    --------
    |      |
    |      O
    |     /|\\
    |      |
    |     / \\ 
    ----|
    """,
    ]
    return stages[tries]
