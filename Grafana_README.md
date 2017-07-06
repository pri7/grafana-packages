# Building Grafana from Source
The following are the steps for building Grafana from source on a linux machine:
## Steps involved:

* Preparing Workspace
* Retrieving Grafana Souce
* Installing Required Dependencies and Building Grafana
* Modifying the Grafana Interface
* Building Packages


### Preparing Workspace

Go requires the following dependencies:

* [Go `v1.8.1`]()
* [NodeJS `LTS`]()
* [Git]()




1. ##### Setting up `Go`
	A hassle free way of setting up `Go`:

	_[The GitHub Repo used](https://github.com/udhos/update-golang)_

	```
	#### after changingworking  to directory ####
	git clone https://github.com/udhos/update-golang
	cd update-golang
	sudo RELEASE=1.8.1 ./update-golang.sh
	```

	The above installs `Go` (`v1.8.1`) into the workspace. Run the following command to add `Go` to your path:

	```
	source /etc/profile.d/golang_path.sh
	```

2. ##### Setting up `NodeJS`

	```
	curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
	sudo apt-get install -y nodejs
	```

3. ##### Setting up `Git`
	Installed by default; further guide [_here_](https://git-scm.com/downloads)




### Retrieving Grafana from Source and Building

```
#### retrieve present working directory ####
export GOPATH={pwd}
go get github.com/grafana/grafana
```

_You may see an error such as: package github.com/grafana/grafana: `no buildable Go source files.` This is just a warning, and you can proceed with the directions._

```
cd $GOPATH/src/github.com/grafana/grafana
go run build.go setup
go run build.go build
```


### Installing Required Dependencies and Building Grafana

```
sudo npm install -g yarn
sudo yarn install --pure-lockfile
sudo npm install -g grunt-cli

grunt
```

_takes ~2mins to build_

You can run the Grafana server using:

```
./bin/grafana-server
```

### Modifying the Grafana Interface

1. ##### Disabling Alerts
	can be done by editing the `.ini` file:

	```
	#################################### Alerting ############################
	[alerting]
	# Disable alerting engine & UI features
	enabled = false				##### change to <false> from <true>, uncomment by removing <;>
	# Makes it possible to turn off alert rule execution but alerting UI is visible
	;execute_alerts = true
	```

2. ##### Customizing the *Login* page
	can be done by editing the file at `$GOPATH/src/github.com/grafana/grafana/public/app/partials/login.html`

3. ##### Customizing Header
	Custom links can be added by editing `$GOPATH/src/github.com/grafana/grafana/public/app/core/components/navbar/navbar.html`

Changes come into affect only after running `grunt`

### Building Packages

We need to first install `fpm` (effing package manager), which needs `ruby` to be installed

```
sudo apt install ruby
sudo apt install ruby-devel
sudo apt-get install -y adduser libfontconfig

sudo gem install fpm

```


###### Building the packages

The following command builds the required packages:
```
	go run build.go build package
```

_takes ~7mins to build_

CentOS, Debian and GZipped Tarball packages (`.rpm`, `.deb` and `.tar.gz`) are created in the `dist/` directory
