# Gamesaves: what they can learn from cloud engineering

Two years ago, while playing Dead Cells on my then Arch Linux setup [0](00_intro.ipynb), I often wished there was a no fuss, "copy and run" way of playing my games. [1](01_file_transfer.ipynb)
Nerds like us like to play Windows games on Linux using a compatibility layer called Wine. One thing that struck out to me was how Wine isolates
all the resources like system files, libraries and other game resources into one single directory for a specific game. This directory is known
as the wineprefix.

My gripe with the aforementioned technique is that once you start playing the game, the clean installation gets tainted with your progress.
To create a checkpoint, one must choose between copying the entire wineprefix or manually finding progress related files. [2](02_wine_prefix.ipynb)
This is an inconvenience, especially when switching machines, forcing me to lose my progress and run the setups every time I picked up an old game. [3](03_switch_machines.ipynb)

Ideally, I'd want to have the fresh wineprefix on an external storage medium along with a list of saved game states of which I can pick one to resume.
If the progress made in the current run is good, I save it as a checkpoint. Otherwise, I nuke the progress to get the clean wineprefix instead of having to copy and running the setup again. [4](04_external_storage.ipynb)

While this might sound like a problem that can be solved by a version control system like git, the initial commit to track all the files
in the wineprefix will need to compress and calculate the sha256sums of all the objects. Even beefy computers will choke at such a computationally
intensive task. If you have ever worked with a large git repository, you know how annoying it gets to do simple git operations. (notebook 5 not added)

So then, how can we create a layer of separation between the freshly installed game and our progress? Let's start with defining our problem a bit more concretely. [6](06_pause_and_ponder.ipynb)
We want to have a read-only version of the game assets and a writable layer on top to capture changes while the game is running. [7](07_problem_definition.ipynb)

For those in the audience who have worked with cloud infrastructure, this idea might sound strikingly similar to containers. To oversimplify, containers
are a bunch of unshare calls to the Linux kernel to fake a different environment by unsharing namespaces such as the mount, process ID, or the network
namespace. [8](08_what_are_containers.ipynb)

The observation to make here is that when we run a container from an image such as alpine, we get access to a fully hierarchical filesystem that allows file modifications. [9](09_notable_idea.ipynb)
Upon removing and restarting the container, however, those modifications are wiped clean, yielding the clean setup as defined in the image. [10](10_restart_container.ipynb)

Docker, the most popular container engine, employs something called the overlay filesystem to create this layer for us to work with until the container gets removed.
An overlay filesystem consists of a read-only lower directory, a writeable upper directory and a scratch working directory to keep track of changed objects; all of
which gets combined into a "merged" directory during runtime.

Sounds an awful lot like our problem definition, doesn't it? [11](11_overlayfs_intro.ipynb)

Let's put this idea to the test! First, we create the upper and work directories using the `mkdir` command.
We rename the wineprefix with the game to be the lower directory. Finally, we run the mount command with the filesystem type - overlay, to layer all of these into the merged target. [12](12_vanilla_mount.ipynb)

But of course, the command fails! We need superuser privileges for the mount operation. While we could use the `sudo` command, elevating our privileges to the superuser, root,
just to play a game feels like an overkill. Besides, running commands as the superuser opens us up to unnecessary security risks. There's no way of mounting vanilla overlayfs in the userspace. [13](13_sudo.ipynb)

Two years ago, this is where I would have ended this video. [14](14_two_years_ago.ipynb)

But let's take a step back [15](15_a_step_back.ipynb), docker isn't the only containerization engine. Podman, a drop-in replacement for docker, is able to run
rootless userspace containers without needing a privileged daemon process running in the background. [16](16_not_the_only.ipynb) At this point, the keen listeners amongst you might have the same question that I did:
"If podman can run rootless containers, how does it mount an overlay filesystem?" [17](17_billion_dollar_question.ipynb)

This is where I'd have to introduce you to a feature of the Linux kernel known as Filesystem in Userspace or FUSE. This interface allows secure and non-privileged mounts. Specifically, podman
achieves userspace overlays using fuse-overlayfs. There's also a convenient commandline tool with the same name that we can install to mount our own overlays. [18](18_fuse_mount.ipynb) So, let's try it out!

We will run fuse-overlayfs with the same options as the previous mount command.

And that merges the directories! [19](19_podmans_secret.ipynb)

Under the hood, the fuse-overlay filesystem reads all the directories as layers along with any user id and group id mappings. It creates a directory called "work" inside the work directory we specify.
All of these are used to create a fuse session which passes the read and write system calls to the respective layers. [20](20_under_the_hood.ipynb)

Running the game from the merged directory causes any new file changes get accumulated in the upper directory. We can unmount this using the fusermount command once we're
done playing for the day. [21](21_unmount.ipynb)
