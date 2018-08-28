load testdata.txt
y=testdata(:,2:end);
path=zeros(22,2);
cx=1;
cy=1;
for x=1:22
    path(x,1)=testdata(x,1);
    path(x,2)=testdata(x,2)
end
robotCurrentLocation = path(1,:);
robotGoal = path(end,:);
initialOrientation = 0;
robotCurrentPose = [robotCurrentLocation initialOrientation];
robotRadius = 0.4;
robot = ExampleHelperRobotSimulator('emptyMap',2);
robot.enableLaser(false);
robot.setRobotSize(robotRadius);
robot.showTrajectory(true);
robot.setRobotPose(robotCurrentPose);
plot(path(:,1), path(:,2),'k--d')
xlim([9 17])
ylim([5 15])
controller = robotics.PurePursuit
controller.Waypoints = path;
controller.DesiredLinearVelocity = 0.3;
controller.MaxAngularVelocity = 2;
controller.LookaheadDistance = 0.5;
goalRadius = 0.1;
distanceToGoal = norm(robotCurrentLocation - robotGoal);
controlRate = robotics.Rate(10);
while( distanceToGoal > goalRadius )
    [v, omega] = controller(robot.getRobotPose);
    drive(robot, v, omega);
    robotCurrentPose = robot.getRobotPose;
    distanceToGoal = norm(robotCurrentPose(1:2) - robotGoal);
    waitfor(controlRate);
end
