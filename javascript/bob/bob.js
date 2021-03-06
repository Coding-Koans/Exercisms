//passes all tests.
class Bob {
    constructor() { }
    hey(input) {

        var taciturn = /^\s*$/,
            shouting = /(^[A-Z\s]*.{0,1}$|^[^a-z]*!$)/,
            question = /\?$/;

        if (input.search(taciturn) !== -1) {
            return "Fine. Be that way!";
        }
        else if (input.search(shouting) !== -1) {
            return "Whoa, chill out!";
        }
        else if (input.search(question) !== -1) {
            return "Sure.";
        }
        else { return "Whatever."; }

    }
}


export default Bob;

//Ok, the last one might have has a use for RegEx, 
//but this one can't live without them.