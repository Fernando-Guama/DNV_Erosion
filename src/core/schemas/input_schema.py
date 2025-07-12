{
  "calculation_request": {
    "metadata": {
      "request_id": "unique_identifier",
      "timestamp": "2024-01-15T10:30:00Z",
      "description": "Erosion calculation for production line",
      "units": "SI"
    },
    "system_conditions": {
      "pressure": {
        "value": 50.0,
        "unit": "bar"
        "calculate": false
      },
      "temperature": {
        "value": 80.0,
        "unit": "celsius"
        "calculate": false
      }
    },
    "fluid_properties": {
      "oil": {
        "density_std": {
          "value": 800.0,
          "unit": "kg/m3"
        },
        "rate_std": {
          "value": 1000.0,
          "unit": "m3/h"
        },
        "viscosity": {
          "value": 0.001,
          "unit": "kg/ms",
        }
      },
      "water": {
        "density_std": {
          "value": 1025.0,
          "unit": "kg/m3"
        },
        "rate_std": {
          "value": 1000.0,
          "unit": "m3/h"
        },
        "viscosity": {
          "value": 0.001,
          "unit": "kg/ms",
        }
      },
      "gas": {
        "density_std": {
          "value": 1025.0,
          "unit": "kg/m3"
        },
        "rate_std": {
          "value": 1000.0,
          "unit": "m3/h"
        },
        "viscosity": {
          "value": 0.001,
          "unit": "kg/ms",
        }
      },
    },
    "sand_properties": {
      "concentration": {
        "value": 10.0,
        "unit": "ppmW"
      },
      "particle_size": {
        "d50": {
          "value": 250.0,
          "unit": "micrometers"
        },
        "distribution": "normal"
      },
      "density": {
        "value": 2650.0,
        "unit": "kg/m3"
      },
      "type": "quartz_sand"
    },
    "components": [
      {
        "id": "component_001",
        "type": "pipe_bend",
        "material": {
          "type": "carbon_steel",
          "density": {
            "value": 7800.0,
            "unit": "kg/m3"
          },
          "erosion_constant_k": {
            "value": 2.0e-9,
            "unit": "(m/s)^-n"
          },
          "velocity_exponent_n": {
            "value": 2.6,
            "unit": "dimensionless"
          }
        },
        "geometry": {
          "internal_diameter": {
            "value": 0.1,
            "unit": "m"
          },
          "radius_of_curvature": {
            "value": 1.5,
            "unit": "pipe_diameters"
          }
        },
        "operating_conditions": {
          "geometry_factor": {
            "value": 1.0,
            "unit": "dimensionless"
          }
        }
      },
      {
        "id": "component_002",
        "type": "straight_pipe",
        "material": {
          "type": "stainless_steel_316",
          "density": {
            "value": 8000.0,
            "unit": "kg/m3"
          },
          "erosion_constant_k": {
            "value": 2.0e-9,
            "unit": "(m/s)^-n"
          },
          "velocity_exponent_n": {
            "value": 2.6,
            "unit": "dimensionless"
          }
        },
        "geometry": {
          "internal_diameter": {
            "value": 0.1,
            "unit": "m"
          },
          "length": {
            "value": 50.0,
            "unit": "m"
          }
        }
      },
      {
        "id": "component_003",
        "type": "welded_joint",
        "material": {
          "type": "carbon_steel",
          "density": {
            "value": 7800.0,
            "unit": "kg/m3"
          },
          "erosion_constant_k": {
            "value": 2.0e-9,
            "unit": "(m/s)^-n"
          },
          "velocity_exponent_n": {
            "value": 2.6,
            "unit": "dimensionless"
          }
        },
        "geometry": {
          "internal_diameter": {
            "value": 0.1,
            "unit": "m"
          },
          "weld_height": {
            "value": 0.002,
            "unit": "m"
          },
          "impact_angle": {
            "value": 60.0,
            "unit": "degrees"
          }
        }
      },
      {
        "id": "component_004",
        "type": "blinded_tee",
        "material": {
          "type": "duplex_steel",
          "density": {
            "value": 7850.0,
            "unit": "kg/m3"
          },
          "erosion_constant_k": {
            "value": 2.0e-9,
            "unit": "(m/s)^-n"
          },
          "velocity_exponent_n": {
            "value": 2.6,
            "unit": "dimensionless"
          }
        },
        "geometry": {
          "internal_diameter": {
            "value": 0.1,
            "unit": "m"
          }
        }
      },
      {
        "id": "component_005",
        "type": "reducer",
        "material": {
          "type": "carbon_steel",
          "density": {
            "value": 7800.0,
            "unit": "kg/m3"
          },
          "erosion_constant_k": {
            "value": 2.0e-9,
            "unit": "(m/s)^-n"
          },
          "velocity_exponent_n": {
            "value": 2.6,
            "unit": "dimensionless"
          }
        },
        "geometry": {
          "inlet_diameter": {
            "value": 0.15,
            "unit": "m"
          },
          "outlet_diameter": {
            "value": 0.1,
            "unit": "m"
          },
          "angle": {
            "value": 30.0,
            "unit": "degrees"
          }
        }
      },
      {
        "id": "component_006",
        "type": "erosion_probe",
        "material": {
          "type": "stainless_steel_316",
          "density": {
            "value": 8000.0,
            "unit": "kg/m3"
          },
          "erosion_constant_k": {
            "value": 2.0e-9,
            "unit": "(m/s)^-n"
          },
          "velocity_exponent_n": {
            "value": 2.6,
            "unit": "dimensionless"
          }
        },
        "geometry": {
          "pipe_diameter": {
            "value": 0.1,
            "unit": "m"
          },
          "probe_angle": {
            "value": 45.0,
            "unit": "degrees"
          }
        }
      }
    ],
    "calculation_options": {
      "time_period": {
        "value": 1.0,
        "unit": "year"
      },
      "include_geometry_factors": true,
      "detailed_output": true,
      "validate_inputs": true
    }
  }
}
