import matplotlib.pyplot as plt
import geopandas as gpd


def plot_map_with_geometry(coords,
                           shapefile_path=r"C:\git\DigitalHunter2\maps_data\ne_50m_admin_0_countries.shp"):
    countries = gpd.read_file(shapefile_path)

    fig, ax = plt.subplots(figsize=(8, 10))
    x_tupl, y_tupl = zip(*coords)
    xmin, xmax, ymin, ymax = min(x_tupl), max(x_tupl), min(y_tupl), max(y_tupl)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect('equal', adjustable='datalim')

    aoi = countries.cx[xmin:xmax, ymin:ymax]
    aoi.plot(ax=ax, color="lightgray", edgecolor="white")

    for idx, row in aoi.iterrows():
        centroid = row.geometry.centroid
        ax.annotate(text=row['ADMIN'], xy=(centroid.x, centroid.y),
                    ha='center', fontsize=8, color='black')

    if len(coords) == 1:
        x, y = coords[0]
        ax.plot(x, y, marker='o', color='red', markersize=8, label='Point')
    elif len(coords) > 1:
        x_coords, y_coords = zip(*coords)
        ax.plot(x_coords, y_coords, color='blue', linewidth=1, label='Path')
        ax.scatter(x_coords[0], y_coords[0], color='green', s=20)  # הצגת הנקודות על הקו
        ax.scatter(x_coords[-1], y_coords[-1], color='red', s=20)
    plt.title('Map View')
    plt.legend()
    plt.show()


