from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    can_iface = LaunchConfiguration("can_iface")
    node_id = LaunchConfiguration("node_id")

    base_launch = PathJoinSubstitution(
        [FindPackageShare("silverhand_arm_control"), "launch", "silverhand_arm_bringup.launch.py"]
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "can_iface",
                default_value="vcan1.0",
                description="Linux CAN interface used by the Cyphal transport.",
            ),
            DeclareLaunchArgument(
                "node_id",
                default_value="100",
                description="Cyphal node id for the ros2_control hardware node.",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(base_launch),
                launch_arguments={
                    "use_mock_hardware": "false",
                    "can_iface": can_iface,
                    "node_id": node_id,
                }.items(),
            ),
        ]
    )
