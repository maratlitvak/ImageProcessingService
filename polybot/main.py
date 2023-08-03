from img_proc import Img

if __name__ == '__main__':

   try:
      my_img = Img('test/beatles.jpeg')
      my_img2 = my_img.save_img(my_img.rotate())

      my_img3 = Img('test/beatles2.jpeg')
      if (len(my_img3.data) != len(my_img.data)):
         raise RuntimeError
      if (len(my_img3.data[0]) != len(my_img.data[0])):
         raise RuntimeError

      my_img4 = my_img3.save_img(my_img3.concat(my_img))
   except:
      raise RuntimeError
   finally:
      my_img.close()

