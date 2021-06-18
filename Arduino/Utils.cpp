#include "Utils.h"

// Alternate row direction to accomodate lightstrip winding, vertical flip and adjust upperleft corner if needed
int pt_finder(int x, int y, int cornershift)
{
  x -= cornershift;
  y = 19 - (y - cornershift);

  if(y%2 == 1)
  {
    x = 24 - x;
  }
  return x + 25*y;
}
