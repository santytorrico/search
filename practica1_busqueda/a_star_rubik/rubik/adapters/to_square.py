from rubik.adapters.adapter import CubeAdapter

class ToSquare(CubeAdapter):
    def __init__(self, face_dict, value_map=None, face_order=None, prepend_face=False, fill_with='', wrap_with=None):
        super().__init__(face_dict)
        self.value_map = value_map
        self.face_order = face_order or ['U', 'L', 'F', 'R', 'B', 'D']
        self.prepend_face = prepend_face
        self.fill_with = fill_with
        self.wrap_with = wrap_with

    def adapt(self):
        result = []
        for face in self.face_order:
            face_data = ''.join([''.join(row) for row in self.face_dict[face]])
            if self.value_map:
                face_values = [self.value_map[char] for char in face_data]
                separator = self.fill_with if self.fill_with else ','
                face_data = separator.join(face_values)
            else:
                separator = self.fill_with if self.fill_with else ''
                face_data = separator.join(face_data)
            if self.prepend_face:
                face_data = face + face_data
            if self.wrap_with:
                face_data = self.wrap_with[0] + face_data + self.wrap_with[1]
            result.append(face_data)
        return '\n'.join(result)
