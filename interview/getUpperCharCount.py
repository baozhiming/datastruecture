import random
import traceback


class Solution:
    @staticmethod
    def get_upper_char_count(file_path: str) -> int:
        upper_char_count = 0
        try:
            with open(file_path, 'r', encoding='utf-8') as fin:
                for line in fin.readlines():
                    for char in line:
                        if char.isupper():
                            upper_char_count += 1
        except Exception:
            raise Exception(f"Solution.get_upper_char_count method error: {traceback.format_exc()}")
        return upper_char_count


def test_get_upper_char_count():
    file_path = "test.csv"
    random_handler = random.Random()

    random_char = [chr(random_handler.randrange(49, 126, 1)) for _ in range(100)]
    with open(file_path, 'w', encoding='utf-8') as fout:
        for i in random_char:
            fout.write(i)
    re = Solution.get_upper_char_count(file_path)
    print(re)
