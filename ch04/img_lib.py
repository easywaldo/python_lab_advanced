"""
패키지 작성
>> 정적이미지(jpg, png) -> gif(애니메이션) 이미지 변환 패키지
"""

import glob
from PIL import Image

# 이미지, 결과 생성 경로
path_in = './project/images/*.png'
path_out = './project/image_out/result.gif'

# 첫번째 이미지 & 모든 이미지 리스트 팩킹
img, *images = [Image.open(f).resize((320, 200), Image.ANTIALIAS) for f in sorted(glob.glob(path_in))]
print(img)
print(images)

# 이미지 저장
img.save(fp=path_out, format='GIF', append_images=images, save_all=True, duration=350, loop=0)

