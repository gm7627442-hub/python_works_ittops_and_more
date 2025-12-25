def create_bottle(capacity=4, initial_volume=0):
    class Bottle:
        pass
    
    bottle = Bottle()
    bottle.capacity = capacity
    bottle.current_volume = min(initial_volume, capacity)  # Не больше ёмкости
    
    return bottle