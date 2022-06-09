from reader_generator import ReaderGenerator

if __name__ == "__main__":
    generator = ReaderGenerator('files\\')
    print(generator.generate(['Lunges', 'PushPress', 'PushUps'], 3))