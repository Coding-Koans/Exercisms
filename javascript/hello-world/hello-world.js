
class HelloWorld {
    constructor() { }
    hello(name) {
        if (name) {
            return ("Hello, " + name + "!");
        } else {
            return "Hello, World!";
        }
    }
}


export default HelloWorld;