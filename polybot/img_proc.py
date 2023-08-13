from pathlib import Path
from matplotlib.image import imread, imsave


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


class Img:
    def __init__(self, path):
        """
        Do not change the constructor implementation
        """
        self.path = Path(path)
        self.data = rgb2gray(imread(path)).tolist()

    def save_img(self, pictrs_arr):
        """
        Do not change the below implementation
        """
        new_path = self.path.with_name(self.path.stem + '_filtered' + self.path.suffix)
        imsave(new_path, pictrs_arr, cmap='gray')
        return new_path

    def blur(self, blur_level=16):
        height = len(self.data)
        width = len(self.data[0])
        filter_sum = blur_level ** 2

        result = []
        for i in range(height - blur_level + 1):
            row_result = []
            for j in range(width - blur_level + 1):
                sub_matrix = [row[j:j + blur_level] for row in self.data[i:i + blur_level]]
                average = sum(sum(sub_row) for sub_row in sub_matrix) // filter_sum
                row_result.append(average)
            result.append(row_result)

        self.data = result
        return self

    def contour(self):
        for i, row in enumerate(self.data):
            res = []
            for j in range(1, len(row)):
                res.append(abs(row[j-1] - row[j]))

            self.data[i] = res
        return self

    def rotate(self):
        rot_img = []
        tmp_lst = []

        for col in range(len(self.data[0])):
            for list_no in range(len(self.data)):
                tmp_lst.append(self.data[list_no][col])

            tmp_lst.reverse()
            rot_img.append(tmp_lst)
            tmp_lst = []
        return rot_img

    def salt_n_pepper(self):
        rot_img = []
        tmp_lst = []

        for col in range(len(self.data[0])):
            for list_no in range(len(self.data)):
                tmp_lst.append(self.data[list_no][col])

            tmp_lst.reverse()
            rot_img.append(tmp_lst)
            tmp_lst = []
        return rot_img

    def concat(self, other_img, direction='horizontal'):
        concat_img = []
        if direction == 'horizontal':
            for i in range(len(self.data)):
                for j in range(len(other_img.data)):
                    self.data[i].append(other_img.data[i][j])
            return self.data
        else:
            for i in range(len(self.data)):
                concat_img.append(self.data[i])

            for i in range(len(other_img.data)):
                concat_img.append(other_img.data[i])
            return concat_img

    def segment(self):
        rot_img = []
        tmp_lst = []

        for col in range(len(self.data[0])):
            for list_no in range(len(self.data)):
                tmp_lst.append(self.data[list_no][col])

            tmp_lst.reverse()
            rot_img.append(tmp_lst)
            tmp_lst = []
        return rot_img
