import wave
import struct
source = wave.open("in.wav", mode="rb")
dest = wave.open("out.wav", mode="wb")
dest.setparams(source.getparams())
frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
data1 = data[::-1]
newframes = struct.pack("<" + str(len(data1)) + "h", *data1)
dest.writeframes(newframes)
source.close()
dest.close()