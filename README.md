# The Architect theme

*This is a [Pelican](https://blog.getpelican.com/) port of the popular [Architect](https://github.com/pages-themes/architect) Jekyll theme for GitHub Pages. You can [preview the theme to see what it looks like](http://pages-themes.github.io/architect), or even [use it today](#usage).*

![Thumbnail of Architect](thumbnail.png)

## Usage

To use the Architect theme:

1. If you don't have `webassets` and `cssmin` installed, you'll need to install them. You can do so by running:
   ```{bash}
   pip install -r requirements.txt
   ```
2. Copy the `themes\architect` folder to your own Pelican blog.
3. Copy the variables from the `pelicanconf.py` folder. The following lines are particularly important:
   ```{python}
   # Set theme
   THEME = 'themes/architect'
   
   # Load plugins
   PLUGIN_PATHS = ['plugins']
   PLUGINS = ['assets']
   
   # Let the assets plugin deal with css
   IGNORE_FILES = ['*.css']
   ```
## Previewing the theme locally
If you'd like to preview the theme locally (for example, in the process of proposing a change):

1. Clone down the theme's repository (git clone https://github.com/MattWThomas/architect-pelican.git)
2. cd into the theme's directory
3. Run the following to install necessary dependencies:
   ```{bash}
   pip install -r requirements.txt
   ```
4. Run `pelican content` to generate the files.
5. Run `pelican --listen ./output` to start the preview server
6. Visit localhost:8000 in your browser to preview the theme


