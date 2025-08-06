class Solution:
    def maximumSwap(self, num: int) -> int:
        swap_num = num
        for i in range(len(list(str(num)))):
            for j in range(len(list(str(num)))):
                #swap
                new_num = swapchars(num,i,j)
                if swap_num < new_num:
                    swap_num = new_num
        return swap_num


def swapchars(num: int, i: int, j: int) -> int:
    char_list = list(str(num))
    aux = char_list[i]
    char_list[i] = char_list[j]
    char_list[j] = aux
    return int("".join(char_list))