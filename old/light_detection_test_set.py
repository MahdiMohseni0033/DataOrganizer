import os
import shutil

mother_path = r'E:\MahdiMohseni\storage\light_source_detection_whole_project\V2\V2_images'
destination_path = r'E:\MahdiMohseni\storage\light_detection_test_sets\V1'


def transformer(l):
    tmp = []
    for i in l:
        tmp.append(str(i) + '.jpg')
    return tmp


def main():
    # prespective = [3741, 3765, 3794, 3856, 3896, 3900, 3909, 3985, 3988, 4012, 4186]
    # low_light_windows = [3839, 3843, 3931, 3939, 3942, 3943, 3962, 3963, 3981, 4014, 4066]
    # objects = [3809, 3847, 3887, 3940, 4006, 4149]
    # tricky_lights = [3745, 3760, 3804, 3821, 3832, 3837, 3912, 3982, 4008, 4048]

    prespective = []
    low_light_windows = [4128, 4489, 4404, 4575]
    objects = [4052, 4054, 4082, 4136, 4181, 4213, 4284, 4301, 4328, 4390, 4436, 4446, 4702, 4712, 4806]
    tricky_lights = [4092, 4135, 4148, 4162, 4225, 4267, 4347, 4357, 4422, 4472, 4488, 4502, 4527, 4559, 4601, 4661,
                     4775]

    prespective = transformer(prespective)
    low_light_windows = transformer(low_light_windows)
    objects = transformer(objects)
    tricky_lights = transformer(tricky_lights)

    for i in prespective:
        src = os.path.join(mother_path, i)
        dst = os.path.join(destination_path, 'prespective')
        shutil.copy(src, dst)

    for i in low_light_windows:
        src = os.path.join(mother_path, i)
        dst = os.path.join(destination_path, 'low_light_windows')
        shutil.copy(src, dst)

    for i in objects:
        src = os.path.join(mother_path, i)
        dst = os.path.join(destination_path, 'objects')
        shutil.copy(src, dst)

    for i in tricky_lights:
        src = os.path.join(mother_path, i)
        dst = os.path.join(destination_path, 'tricky_lights')
        shutil.copy(src, dst)


if __name__ == '__main__':
    main()
