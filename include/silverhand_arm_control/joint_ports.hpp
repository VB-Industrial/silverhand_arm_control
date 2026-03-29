#ifndef SILVERHAND_ARM_CONTROL__JOINT_PORTS_HPP_
#define SILVERHAND_ARM_CONTROL__JOINT_PORTS_HPP_

#include <array>
#include <cstdint>

namespace silverhand_arm_control
{

constexpr std::size_t kJointCount = 6;
constexpr std::uint16_t kAgentJointStatePort = 1001;

constexpr std::array<std::uint16_t, kJointCount> kJointCommandPorts = {
  1121,
  1122,
  1123,
  1124,
  1125,
  1126,
};

}  // namespace silverhand_arm_control

#endif  // SILVERHAND_ARM_CONTROL__JOINT_PORTS_HPP_
