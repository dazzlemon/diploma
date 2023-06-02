rm -rf build/linux
cp -r src build/linux

gcc \
  build/main.c \
  -I/usr/include/python3.10 \
	-lpython3.10 \
	-o build/linux/main
