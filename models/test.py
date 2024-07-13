def reverse(text):
  text = text.strip()
  text_list = text.split(' ')
  text_list_reverse = text_list[::-1]
  # text_list_reverse = []
  # for part in text_list_reverse:
  #     text_list_reverse.append(part)
  result = ' '.join(text_list_reverse)
  return result
if __name__=='__main__':
  s = "the sky is blue"
  result = reverse(s)
  print(result)
