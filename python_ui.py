import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class User():
    def __init__(self, email, password, file):
        self.email = email
        self.password = password
        self.file = file


class SignInMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="Sign In")
        self.set_border_width(10)

        self.timeout_id = None

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        self.label = Gtk.Label()
        self.label.set_markup('<big><b>Make your login...</b></big>')
        self.vbox.pack_start(self.label, True, True, 0)

        self.hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.vbox.pack_start(self.hbox1, True, True, 0)

        self.email = Gtk.Entry()
        self.email.set_size_request(180, 30)
        self.text_email = Gtk.Label(label="Email:")
        self.hbox1.pack_start(self.text_email, True, True, 0)
        self.hbox1.pack_start(self.email, True, True, 0)

        self.hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.vbox.pack_start(self.hbox2, True, True, 0)

        self.password = Gtk.Entry()
        self.password.set_size_request(112, 30)
        Gtk.Entry.set_visibility(self.password, False)
        self.text_pass = Gtk.Label(label="Password:")
        self.hbox2.pack_start(self.text_pass, True, True, 0)
        self.hbox2.pack_start(self.password, True, True, 0)


        self.register = Gtk.Button(label="Sign In")
        self.register.connect("clicked", self.log_in)
        self.vbox.pack_start(self.register, True, True, 0)

    def log_in(self, widget):
        try:
            if ((user.email == self.email.get_text()) and (user.password == self.password.get_text())):
                print("You are logged in")
                self.close()
            else:
                print("Something was wrong... Check your credentials and try again")
        except:
            print("Make your register first!!")


class SignUpMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="Sign Up")
        self.set_border_width(10)

        self.timeout_id = None

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        self.label = Gtk.Label()
        self.label.set_markup('<big><b>Make your register to sign in!</b></big>')
        self.vbox.pack_start(self.label, True, True, 0)

        self.hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.vbox.pack_start(self.hbox1, True, True, 0)

        self.email = Gtk.Entry()
        Gtk.Entry.set_placeholder_text(self.email,"email@email.com")
        self.email.set_size_request(240, 30)
        self.text_email = Gtk.Label(label="*Email:")
        # self.text_email.set_justify(Gtk.Justification.LEFT)
        self.hbox1.pack_start(self.text_email, True, True, 0)
        self.hbox1.pack_start(self.email, True, True, 0)

        self.hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.vbox.pack_start(self.hbox2, True, True, 0)

        self.password = Gtk.Entry()
        Gtk.Entry.set_placeholder_text(self.password,"password")
        self.password.set_size_request(220, 30)

        self.text_pass = Gtk.Label(label="*Password:")
        # self.text_pass.set_justify(Gtk.Justification.LEFT)
        self.hbox2.pack_start(self.text_pass, True, True, 0)
        Gtk.Entry.set_visibility(self.password, False)
        self.hbox2.pack_start(self.password, True, True, 0)

        self.hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.vbox.pack_start(self.hbox3, True, True, 0)

        self.text_file = Gtk.Label(label="*Profile Photo:")
        self.file = Gtk.FileChooserButton()
        self.file.set_size_request(200, 30)
        self.hbox3.pack_start(self.text_file, True, True, 0)
        self.hbox3.pack_start(self.file, True, True, 0)

        self.register = Gtk.Button(label="Sign Up")
        self.register.connect("clicked", self.make_register)
        self.vbox.pack_start(self.register, True, True, 0)

    def verify_email(self):
        email = self.email.get_text()

        if email.__contains__('@') and email.__contains__('.com'):
            return True
        return False

    def make_register(self, widget):
        verification = self.verify_email()
        if (verification):
            if ((self.email is not None) and (self.password is not None) and (self.file.get_filename() is not None)):
                global user
                user = User(self.email.get_text(), self.password.get_text(), self.file.get_file())
                print('Register was succeeded!')
                self.close()
            else:
                print('Some of the fields are empty, please check it and try again')
        else:
            print("Something was wrong... Check your credentials and try again")


class MainMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="HappytAuth")
        self.set_border_width(10)
        self.set_size_request(300, 50)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        self.label = Gtk.Label()
        self.label.set_markup('<big><b>Be welcome to our application!</b></big>')
        self.vbox.pack_start(self.label, True, True, 0)

        self.box = Gtk.Box(spacing=6)
        self.vbox.pack_start(self.box, True, True, 0)

        self.signUp = Gtk.Button(label="Sign Up")
        self.signUp.connect("clicked", self.sign_up)
        self.box.pack_start(self.signUp, True, True, 0)

        self.signIn = Gtk.Button(label="Sign In")
        self.signIn.connect("clicked", self.sign_in)
        self.box.pack_start(self.signIn, True, True, 0)

    def sign_up(self, widget):
        win = SignUpMenu()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def sign_in(self, widget):
        win = SignInMenu()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()


win = MainMenu()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()