function letterCombinations(digits: string): string[] {
    // Edge case: if the input is empty, return an empty array
    if (digits.length === 0) return [];

    // Create a hash map to map digits to their corresponding letters
    const digitToLetters: { [key: string]: string } = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    };

    // Result array to store all combinations
    const result: string[] = [];

    // Backtracking function to generate combinations
    const backtrack = (index: number, currentCombination: string) => {
        // Base case: if the current combination is complete, add it to the result
        if (index === digits.length) {
            result.push(currentCombination);
            return;
        }

        // Get the current digit and its corresponding letters
        const currentDigit = digits[index];
        const letters = digitToLetters[currentDigit];

        // Iterate through all letters and recursively build the combination
        for (let i = 0; i < letters.length; i++) {
            backtrack(index + 1, currentCombination + letters[i]);
        }
    };

    // Start the backtracking process
    backtrack(0, '');

    return result;
}
