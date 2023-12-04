#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print(f"Original position: {alien_0['x_position']}")

# Move alien to the right.
# Determine how far to move the alien based on its current speed.
#if alien_0['speed'] == 'slow':
    #x_increment = 1
#elif alien_0['speed'] == 'medium':
    #x_increment = 2
#else:
    # This must be a fast alien.
    #x_increment = 3

# The new position is the old position plus the increment.
#alien_0['x_position'] = alien_0['x_position'] + x_increment

#print(f"New position: {alien_0['x_position']}")

aliens = []

#make 30 green aliens.
for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:3]:
    if alien['color'] =='green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show ow many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


