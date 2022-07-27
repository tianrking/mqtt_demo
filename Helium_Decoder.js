function Decoder(bytes, port) {
    var decoded = {};
    function transformers(bytes) {
        if (bytes[0] == 255 || bytes[0] == 0) {
            value = bytes[2] * 256 + bytes[3];
        }
        return value;
    }
    if (port == 8) {
        decoded.class = transformers(bytes.slice(0, 4));
    }
  var decodedPayload = {
    "class": decoded.class 
  };
  return decodedPayload
}
