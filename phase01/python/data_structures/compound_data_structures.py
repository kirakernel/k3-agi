# chatGPT
programming_langs = {
  'Rust': {
    'Fact1': 'Rust is a statically-typed programming language designed for system-level programming, emphasizing safety and performance.',
    'Fact2': 'It was created by Mozilla and first released in 2010, with a focus on preventing memory-related errors like null pointer dereferences and buffer overflows.',
    'Fact3': 'Rust\'s ownership system, borrowing, and lifetimes contribute to its memory safety without the need for garbage collection.'
  },
  'JavaScript': {
    'Fact1': 'JavaScript is a high-level, interpreted programming language primarily used for building dynamic and interactive web pages.',
    'Fact2': 'It was originally developed by Brendan Eich in 1995 and is now supported by all major web browsers.',
    'Fact3': 'JavaScript is versatile and can be used for both front-end and back-end development, thanks to frameworks like Node.js.'
  },
  'Python': {
    'Fact1': 'Python is a general-purpose, high-level programming language known for its readability, simplicity, and versatility.',
    'Fact2': 'Guido van Rossum created Python, and it was first released in 1991. Python\'s design philosophy emphasizes code readability and ease of use.',
    'Fact3': 'It has a large standard library and a vibrant community, making it suitable for a wide range of applications, from web development to data science and artificial intelligence.'
  }
}

print(programming_langs)
print(programming_langs['JavaScript']['Fact1'])
print(type(programming_langs), type(programming_langs['Rust']))


print([x for x in programming_langs])
#print(programming_langs.items())