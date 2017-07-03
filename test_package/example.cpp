#include <ft2build.h>
#include FT_FREETYPE_H

int main() {
  FT_Library lib;
  FT_Init_FreeType(&lib);
  return 0;
}
