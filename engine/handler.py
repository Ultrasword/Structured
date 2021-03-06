"""
File for object types in the engine
"""

ID_COUNTER = 0

def get_object_id():
    """get an object id"""
    global ID_COUNTER
    ID_COUNTER += 1
    return ID_COUNTER



class PersistentObject:
    """
    Objects are things that will be used to render in game entities
    they should not be used to create non-rendered objects

    Objects include:
    - entities
    - persistent effects

    Not include:
    - particles
    - background effects
    
    """
    def __init__(self):
        """ Constructor for Object class"""
        self.object_id = 0
    
    @property
    def id(self):
        """Get the object id"""
        return self.object_id
    
    def update(self, dt):
        """Default update method"""
        pass
    
    def handle_changes(self):
        """Default handle changes method"""
        pass
    
    def render(self):
        """Default render function"""
        pass


class Handler:
    """
    A persistent object and non persistent object handler
    When adding an object, you can either pick an specific type to add
    Or you can just use a default func defined

    Can add
    - entities
    - background effects
    - persistent background effects

    Should not add
    - Particles
    - should use ParticleHandler
    
    """
    def __init__(self):
        """Handler constructor"""
        # for persistent objects
        self.p_objects = {}

        # non persistent objects
        self.objects = {}
        self.non_p_object_counter = 0

        # updates
        self.dirty = True
    
    def get_non_persist_id(self):
        """Generate a non persisting id for this specific handler"""
        self.non_p_object_counter += 1
        return self.non_p_object_counter
    
    def add_persist_entity(self, entity):
        """Add persistent entity"""
        entity.object_id = get_object_id()
        self.p_objects[entity.id] = entity
    
    def add_entity(self, entity):
        """Add non-persisting entity"""
        entity.object_id = get_object_id()
        self.objects[entity.id] = entity
    
    def add_entity_auto(self, entity):
        """Add entity and auto select where it should go"""
        if instanceof(entity, PersistentObject):
            self.p_objects[entity.id] = entity
            entity.object_id = get_object_id()
        else:
            entity.object_id = self.get_non_persist_id()
            self.objects[entity.id] = entity

    def remove_persistent_entity(self, eid):
        """Can only remove persistent entities"""
        if eid in self.p_objects:
            self.p_objects.pop(eid)
    
    def remove_entity(self, eid):
        """Can only remove non-persisting entities"""
        if eid in self.objects:
            self.objects.pop(eid)
        
    def handle_entities(self, dt):
        """
        Handle entities
        
        1. Update entities
            - pass through dt
        2. Render entities
            - pass through window
        """
        for eid, entity in self.p_objects.items():
            entity.update(dt)
            entity.handle_changes()
            entity.render()
        
        for eid, entity in self.objects.items():
            entity.update(dt)
            entity.handle_changes()
            entity.render()

    def render_all(self):
        """Render all entities in case needed to"""
        # usually used when window resized
        for eid, entity in self.p_objects.items():
            entity.dirty = True
            entity.render()
        
        for eid, entity in self.objects.items():
            entity.dirty = True
            entity.render()




