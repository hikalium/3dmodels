BLENDER_URL=https://mirror.freedif.org/blender/release/Blender4.0/blender-4.0.1-linux-x64.tar.xz
BLENDER_PATH=bin/blender-4.0.1-linux-x64/blender

${BLENDER_PATH} :
	mkdir -p bin
	echo ${BLENDER_URL}
	#cd bin && \
	#	wget ${BLENDER_URL}

run : ${BLENDER_PATH}
	${BLENDER_PATH}

