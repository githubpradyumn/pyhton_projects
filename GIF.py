import imageio.v3 as iio
filenames = ['https://raw.githubusercontent.com/codedex-io/projects/main/projects/create-a-gif-with-python/team-pic1.png', 'https://raw.githubusercontent.com/codedex-io/projects/main/projects/create-a-gif-with-python/team-pic2.png']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))
  iio.imwrite('team.gif', images, duration = 500, loop = 0)

