class ElevatorRequests(object):
    def __init__(self):
        self.current_floor = -1
        self.number_of_active_requests = -1


class ElevatorRequest(object):
    def __init__(self, start_floor, goal_floor, command, elevator_id=1, mode='ROBOT', query_id=None,
                 task_id=None, load=None, robot_id=None, status='pending'):
        self.elevator_id = elevator_id
        self.operational_mode = mode

        self.start_floor = start_floor
        self.goal_floor = goal_floor
        self.command = command

        self.query_id = query_id
        self.task_id = task_id
        self.load = load
        self.robot_id = robot_id
        self.status = status

    def to_dict(self):
        request_dict = dict()
        request_dict['elevatorId'] = self.elevator_id
        request_dict['operationalMode'] = self.operational_mode
        request_dict['startFloor'] = self.start_floor
        request_dict['goalFloor'] = self.goal_floor
        request_dict['queryId'] = self.query_id
        request_dict['command'] = self.command
        request_dict['load'] = self.load
        request_dict['robotId'] = self.robot_id
        request_dict['status'] = self.status
        request_dict['taskId'] = self.task_id
        return request_dict

    @staticmethod
    def from_dict(request):
        robot_request = ElevatorRequest()

        robot_request.query_id = request['query_id']
        robot_request.command = request['command']
        robot_request.start_floor = request['startFloor']
        robot_request.goal_floor = request['goalFloor']
        robot_request.task_id = request['taskId']
        robot_request.load = request['load']
        robot_request.robot_id = request['robotId']
        robot_request.status = request['status']
        return robot_request


class Elevator(object):
    def __init__(self):
        self.elevator_id = -1
        self.floor = -1 # TODO: Need to match floors from toma messages to world model ones
        self.calls = -1
        self.is_available = False
        self.door_open_at_goal_floor = False
        self.door_open_at_start_floor = False

    def to_dict(self):
        elevator_dict = dict()
        elevator_dict['elevatorId'] = self.elevator_id
        elevator_dict['floor'] = self.floor
        elevator_dict['calls'] = self.calls
        elevator_dict['isAvailable'] = self.is_available
        elevator_dict['doorOpenAtGoalFloor'] = self.door_open_at_goal_floor
        elevator_dict['doorOpenAtStartFloor'] = self.door_open_at_start_floor
        return elevator_dict

    @staticmethod
    def from_dict(elevator_dict):
        elevator = Elevator()
        elevator.elevator_id = elevator_dict['elevatorId']
        elevator.floor = elevator_dict['floor']
        elevator.calls = elevator_dict['calls']
        elevator.is_available = elevator_dict['isAvailable']
        elevator.door_open_at_goal_floor = elevator_dict['doorOpenAtGoalFloor']
        elevator.door_open_at_start_floor = elevator_dict['doorOpenAtStartFloor']
        return elevator


class RobotCallUpdate(object):
    def __init__(self, query_id, command, elevator_id=1, start_floor=None, goal_floor=None):
        self.queryId = query_id
        self.command = command
        self.elevatorId = elevator_id
        if start_floor:
            self.startFloor = start_floor
        elif goal_floor:
            self.goalFloor = goal_floor
        else:
            raise Exception("Missing goal or start floor")

    def to_dict(self):
        return self.__dict__


class RobotElevatorCallReply(object):
    def __init__(self, query_id, query_success=True, elevator_id=1, elevator_waypoint='door-1'):
        self.queryId = query_id
        self.querySuccess = query_success
        self.elevatorId = elevator_id
        self.elevatorWaypoint = elevator_waypoint

    def to_dict(self):
        return self.__dict__
