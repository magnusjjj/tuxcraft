import packets.KeepAlive
import packets.Handshake
import packets.PlayerPosition
import packets.PlayerLook
import packets.PlayerPositionAndLook
import packets.PlayerDigging
import packets.Animation
import packets.CloseWindow
import packets.ClickWindow
import packets.LocaleAndViewDistance
import packets.ServerListPing

commands = {
		0: packets.KeepAlive.command,
		2: packets.Handshake.command,
		11: packets.PlayerPosition.command,
		12: packets.PlayerLook.command,
		13: packets.PlayerPositionAndLook.command,
		14: packets.PlayerDigging.command,
		18: packets.Animation.command,
		101: packets.CloseWindow.command,
		102: packets.ClickWindow.command,
		204: packets.LocaleAndViewDistance.command,
		254: packets.ServerListPing.command
}
