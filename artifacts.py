# Artifacts
# to be added:     # Lambda function that calls artifact's effect
    # while on the menu, show description ---> after the functionality is completed.
    # all - 'smth' % are rounded up
    # if END reaches 0 -> you take double damage everytime  
common_artifacts = {
  "Vajra" : 
    {
    "effect" : "STR +2",
    "description" : "A sword that gives you strength."
    },

  "Magic Ring" :
    {
    "effect" : "INT +2",
    "description" : "A ring forged by ancient sorcerers."    
    },

  "Iron Armor" :
  {
  "effect" : "END +1",
  "description" : "Heavy, damaged armor."    
  }
}


rare_artifacts = {
  "Blade of Eternity" : 
    {
    "effect" : "STR x2, Max Hp -50%, END -4",
    "description" : "An ancient blade granting immense power."
    },

  "Defender" :
    {
    "effect" : "STR +2, END +2",
    "description" : "Practical sword."    
    },

  "Staff of the Arcane":
    {
    "effect" : "INT x2, Max Hp -40%, END -4",
    "description" : "Channels pure arcane energy, at a cost."   
    },
  
  "Mythril Staff" :
    {
      "effect" : "INT +5",
      "description" : "Made of mythril."
    },

  "Crown of the King":
      {
      "effect": "All Stats +20%, but enemies are more attracted to you",
        "description": "Worn by a ruler that draws attention and power."
        }
}

mythic_artifacts = {
  "Angel's Wings" : 
    {
    "effect" : "Nullifies ",
    "description" : "You cannot recall, but a familiar feeling takes over you, as you begin to cry. The wings wrap around you, providing warmth."
    },

  "Angel's Halo" : 
    {
    "effect" : "Upon death, revive once at HP +1",
    "description" : "You cannot recall, but a familiar feeling takes over you, as you begin to cry. The halo glows, providing warmth."
    }
}
