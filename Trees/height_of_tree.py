def height(self):
    if self.root is not None:
        return self._height(self.root, 0)


def _height(self, cur_level, tree_height):
    if cur_level is None:
        return tree_height
    left_height = self._height(cur_level.left_child, tree_height + 1)
    right_height = self._height(cur_level.right_child, tree_height + 1)
    return max(left_height, right_height)