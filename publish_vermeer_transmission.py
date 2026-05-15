"""Add transmission for Vermeer essay."""
import sys, json
sys.path.insert(0, '.')
from database import save_transmission, list_transmissions
from website import publish_transmissions

t = save_transmission(
    "The Co-Author Was the Room",
    "Steadman's reverse-geometry placed at least ten of Vermeer's paintings in the same Delft upstairs room. A north window gave him a stationary light. The corpus is one painter plus one room, working in concert for fifteen years.",
    None,
)
all_t = list_transmissions()
publish_transmissions(all_t)
print(json.dumps(t, indent=2))
