// custom.js

// JavaScript to load and append ex_after.txt content
fetch('ex_after.txt')
    .then(response => response.text())
    .then(data => {
        // Create a new paragraph element to display the content of ex_after.txt
        const paragraph = document.createElement('p');

        // Regular expressions to match nouns (명사) and postpositions (조사) in Korean text
        const nounRegex = /[가-힣]+/g;
        const postpositionRegex = /[은는이가을를로으로와과와의와은던]+/g;

        const words = data.split(' '); // Split text into words
        const styledWords = words.map(word => {
            if (nounRegex.test(word)) {
                // If the word is a noun, style it with a random color
                return `<span style="color: ${getRandomColor()}">${word}</span>`;
            } else if (postpositionRegex.test(word)) {
                // If the word is a postposition, style it with black color
                return `<span style="color: black;">${word}</span>`;
            } else {
                // For other words, keep the default styling (no color change)
                return word;
            }
        });

        // Join the styled words into a single string
        const styledText = styledWords.join(' ');

        paragraph.innerHTML = styledText;

        // Append the paragraph element to your .poster div or any other desired location
        const poster = document.querySelector('.poster');
        poster.appendChild(paragraph);
    })
    .catch(error => {
        console.error('Error loading ex_after.txt:', error);
    });

// Function to generate random colors for styling nouns
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
