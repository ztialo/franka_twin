from setuptools import setup

package_name = "franka_twin"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Zi Tao Li",
    maintainer_email="zdli@ucsc.edu",
    description="Franka twin package scaffold.",
    license="MIT",
    entry_points={
        "console_scripts": [
            "franka_twin_node = franka_twin.franka_twin_node:main",
        ],
    },
)
