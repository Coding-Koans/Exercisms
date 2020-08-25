import subject from './hello-world';

describe('Hello World', () => {
  test('Say Hi!', () => {
    const instantiated_subject = new subject
    const actual = instantiated_subject.hello()
    expect(actual).toEqual('Hello, World!');
  });
});
