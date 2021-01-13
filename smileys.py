def count_smileys(arr):
    faces = 0
    eyes = [':',';']
    nose = ['-','~']
    mouth = [')','D']
    for smiley in arr:
        if len(smiley) == 3 and smiley[0] in eyes and smiley[1] in nose and smiley[2] in mouth:
            faces += 1
        elif len(smiley) == 2 and smiley[0] in eyes and smiley[1] in mouth:
            faces += 1
    return faces

print(count_smileys([':)', ';(', ';}', ':-D']))