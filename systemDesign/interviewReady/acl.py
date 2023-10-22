import threading


class AccessManager:
    def __init__(self):
        # Initialize an empty nested dictionary to store permissions
        self.permissions = {}
        # Create a reentrant lock to protect concurrent access to the dictionary
        self.lock = threading.RLock()

    def addPermission(self, actionType, userId, objectId):
        # Acquire a lock for writing to the permissions dictionary
        with self.lock:
            # Check if the action type exists in the permissions dictionary
            if actionType not in self.permissions:
                self.permissions[actionType] = {}

            # Check if the user exists in the action type's permissions dictionary
            if userId not in self.permissions[actionType]:
                self.permissions[actionType][userId] = {}

            # Set permission for the user to access the object with the specified action
            self.permissions[actionType][userId][objectId] = True

    def checkPermissions(self, actionType, userId, objectId):
        # Acquire a read lock to safely check permissions in the dictionary
        with self.lock:
            # Check if the action type exists in the permissions dictionary
            if actionType not in self.permissions:
                return False  # Action type not found

            # Check if the user exists in the action type's permissions dictionary
            if userId not in self.permissions[actionType]:
                return False  # User not found

            # Check if the user has permission to access the specified object with the action
            return self.permissions[actionType][userId].get(objectId, False)


# Create a new instance of the AccessManager
access_manager = AccessManager()

# Example usage with adding permissions and checking permissions
access_manager.addPermission("read", "user1", "object1")
access_manager.addPermission("write", "user1", "object2")
access_manager.addPermission("read", "user2", "object1")

print(access_manager.checkPermissions("read", "user1", "object1"))  # Should return True
print(access_manager.checkPermissions("write", "user1", "object1"))  # Should return False
print(access_manager.checkPermissions("read", "user2", "object2"))  # Should return False
