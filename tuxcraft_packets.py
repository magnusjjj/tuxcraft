import packets.KeepAlive
import packets.Handshake
import packets.ChatMessage
import packets.Player
import packets.PlayerPosition
import packets.PlayerLook
import packets.PlayerPositionAndLook
import packets.PlayerDigging
import packets.PlayerBlockPlacement
import packets.Animation
import packets.EntityAction
import packets.CloseWindow
import packets.ClickWindow
import packets.TabCompletion
import packets.LocaleAndViewDistance
import packets.ClientStatuses
import packets.PluginMessage
import packets.ServerListPing

commands = {
		0: packets.KeepAlive.command,
		2: packets.Handshake.command,
		3: packets.ChatMessage.command,
		10: packets.Player.command,
		11: packets.PlayerPosition.command,
		12: packets.PlayerLook.command,
		13: packets.PlayerPositionAndLook.command,
		14: packets.PlayerDigging.command,
		15: packets.PlayerBlockPlacement.command,
		18: packets.Animation.command,
		19: packets.EntityAction.command,
		101: packets.CloseWindow.command,
		102: packets.ClickWindow.command,
		203: packets.TabCompletion.command,
		204: packets.LocaleAndViewDistance.command,
		205: packets.ClientStatuses.command,
		250: packets.PluginMessage.command,
		254: packets.ServerListPing.command
}
