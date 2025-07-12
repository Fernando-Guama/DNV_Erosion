{
  "calculation_response": {
    "metadata": {
      "request_id": "unique_identifier",
      "calculation_timestamp": "2024-01-15T10:30:15Z",
      "processing_time_ms": 245,
      "dnv_rp_version": "O501-2015-amended-2021",
      "calculation_engine_version": "1.0.0"
    },
    "status": {
      "success": true,
      "validation_passed": true,
      "warnings": [],
      "errors": []
    },
    "input_summary": {
      "total_components": 6,
      "component_types": ["pipe_bend", "straight_pipe", "welded_joint", "blinded_tee", "reducer", "erosion_probe"],
      "mixture_velocity": {
        "value": 15.0,
        "unit": "m/s"
      },
      "sand_concentration": {
        "value": 10.0,
        "unit": "ppmW"
      },
      "erosion_class": 3,
      "erosion_class_description": "Medium erosion potential"
    },
    "fluid_calculations": {
      "mixture_properties": {
        "density": {
          "value": 650.0,
          "unit": "kg/m3",
          "calculation_method": "black_oil_model"
        },
        "viscosity": {
          "value": 0.001,
          "unit": "kg/ms",
          "calculation_method": "black_oil_model"
        },
        "velocity": {
          "value": 15.0,
          "unit": "m/s"
        },
        "reynolds_number": {
          "value": 975000.0,
          "unit": "dimensionless"
        }
      },
      "sand_mass_flow": {
        "value": 0.00234,
        "unit": "kg/s"
      }
    },
    "component_results": [
      {
        "component_id": "component_001",
        "component_type": "pipe_bend",
        "status": "success",
        "erosion_calculations": {
          "characteristic_impact_angle": {
            "value": 33.7,
            "unit": "degrees"
          },
          "dimensionless_parameter_A": {
            "value": 2.5,
            "unit": "dimensionless"
          },
          "critical_particle_diameter": {
            "value": 0.00015,
            "unit": "m"
          },
          "particle_correction_factor_G": {
            "value": 0.8,
            "unit": "dimensionless"
          },
          "material_function_F_alpha": {
            "value": 0.9,
            "unit": "dimensionless"
          },
          "model_geometry_factor_C1": {
            "value": 2.5,
            "unit": "dimensionless"
          },
          "geometry_factor": {
            "value": 1.0,
            "unit": "dimensionless"
          }
        },
        "erosion_results": {
          "relative_erosion_rate": {
            "value": 0.025,
            "unit": "mm/ton"
          },
          "annual_erosion_rate": {
            "value": 0.0006,
            "unit": "mm/year"
          },
          "erosion_for_specified_period": {
            "value": 0.0006,
            "unit": "mm"
          },
          "maximum_erosion_location": "40 degrees from bend inlet",
          "erosion_area": {
            "value": 0.00785,
            "unit": "m2"
          }
        },
        "risk_assessment": {
          "risk_level": "low",
          "time_to_1mm_erosion": {
            "value": 1667,
            "unit": "years"
          },
          "sand_required_for_1mm": {
            "value": 40,
            "unit": "tons"
          }
        }
      },
      {
        "component_id": "component_002",
        "component_type": "straight_pipe",
        "status": "success",
        "erosion_calculations": {
          "flow_regime": "turbulent",
          "pipe_orientation": "vertical"
        },
        "erosion_results": {
          "relative_erosion_rate": {
            "value": 0.0001,
            "unit": "mm/ton"
          },
          "annual_erosion_rate": {
            "value": 0.0000024,
            "unit": "mm/year"
          },
          "erosion_for_specified_period": {
            "value": 0.0000024,
            "unit": "mm"
          },
          "maximum_erosion_location": "distributed along pipe",
          "erosion_area": {
            "value": 15.71,
            "unit": "m2"
          }
        },
        "risk_assessment": {
          "risk_level": "negligible",
          "time_to_1mm_erosion": {
            "value": 416667,
            "unit": "years"
          },
          "sand_required_for_1mm": {
            "value": 10000,
            "unit": "tons"
          }
        }
      },
      {
        "component_id": "component_003",
        "component_type": "welded_joint",
        "status": "success",
        "erosion_calculations": {
          "impact_angle": {
            "value": 60.0,
            "unit": "degrees"
          },
          "material_function_F_alpha": {
            "value": 0.78,
            "unit": "dimensionless"
          },
          "particle_correction_factor_C2": {
            "value": 0.85,
            "unit": "dimensionless"
          }
        },
        "erosion_results": {
          "flow_facing_weld": {
            "relative_erosion_rate": {
              "value": 0.008,
              "unit": "mm/ton"
            },
            "annual_erosion_rate": {
              "value": 0.0002,
              "unit": "mm/year"
            },
            "note": "Weld rounding, typically not structural concern"
          },
          "downstream_weld": {
            "relative_erosion_rate": {
              "value": 0.012,
              "unit": "mm/ton"
            },
            "annual_erosion_rate": {
              "value": 0.0003,
              "unit": "mm/year"
            }
          }
        },
        "risk_assessment": {
          "risk_level": "low",
          "critical_location": "downstream of weld"
        }
      },
      {
        "component_id": "component_004",
        "component_type": "blinded_tee",
        "status": "success",
        "erosion_calculations": {
          "particle_diameter_ratio": {
            "value": 0.0025,
            "unit": "dimensionless"
          },
          "density_ratio_beta": {
            "value": 4.08,
            "unit": "dimensionless"
          },
          "reynolds_number": {
            "value": 975000,
            "unit": "dimensionless"
          },
          "critical_particle_diameter": {
            "value": 0.00012,
            "unit": "m"
          },
          "particle_correction_factor": {
            "value": 0.9,
            "unit": "dimensionless"
          },
          "model_factor_C1": {
            "value": 0.3,
            "unit": "dimensionless"
          }
        },
        "erosion_results": {
          "relative_erosion_rate": {
            "value": 0.015,
            "unit": "mm/ton"
          },
          "annual_erosion_rate": {
            "value": 0.00036,
            "unit": "mm/year"
          },
          "erosion_for_specified_period": {
            "value": 0.00036,
            "unit": "mm"
          },
          "maximum_erosion_location": "blind zone center",
          "erosion_area": {
            "value": 0.00785,
            "unit": "m2"
          }
        },
        "risk_assessment": {
          "risk_level": "low",
          "time_to_1mm_erosion": {
            "value": 2778,
            "unit": "years"
          }
        }
      },
      {
        "component_id": "component_005",
        "component_type": "reducer",
        "status": "success",
        "erosion_calculations": {
          "inlet_velocity": {
            "value": 15.0,
            "unit": "m/s"
          },
          "outlet_velocity": {
            "value": 33.75,
            "unit": "m/s"
          },
          "area_ratio": {
            "value": 0.44,
            "unit": "dimensionless"
          },
          "impact_angle": {
            "value": 30.0,
            "unit": "degrees"
          },
          "material_function_F_alpha": {
            "value": 1.0,
            "unit": "dimensionless"
          },
          "particle_correction_factor": {
            "value": 0.85,
            "unit": "dimensionless"
          }
        },
        "erosion_results": {
          "relative_erosion_rate": {
            "value": 0.045,
            "unit": "mm/ton"
          },
          "annual_erosion_rate": {
            "value": 0.00108,
            "unit": "mm/year"
          },
          "erosion_for_specified_period": {
            "value": 0.00108,
            "unit": "mm"
          },
          "maximum_erosion_location": "tapered section",
          "erosion_area": {
            "value": 0.0034,
            "unit": "m2"
          }
        },
        "risk_assessment": {
          "risk_level": "low",
          "time_to_1mm_erosion": {
            "value": 926,
            "unit": "years"
          }
        }
      },
      {
        "component_id": "component_006",
        "component_type": "erosion_probe",
        "status": "success",
        "erosion_calculations": {
          "probe_angle": {
            "value": 45.0,
            "unit": "degrees"
          },
          "material_function_F_alpha": {
            "value": 1.0,
            "unit": "dimensionless"
          },
          "particle_correction_factor": {
            "value": 0.85,
            "unit": "dimensionless"
          },
          "equivalent_impact_area": {
            "value": 0.00785,
            "unit": "m2"
          }
        },
        "erosion_results": {
          "relative_erosion_rate": {
            "value": 0.03,
            "unit": "mm/ton"
          },
          "annual_erosion_rate": {
            "value": 0.00072,
            "unit": "mm/year"
          },
          "erosion_for_specified_period": {
            "value": 0.00072,
            "unit": "mm"
          }
        },
        "monitoring_data": {
          "sand_production_from_erosion": {
            "value": 0.024,
            "unit": "kg/s",
            "note": "Calculated from erosion rate - use only for V_m > 5 m/s"
          }
        },
        "risk_assessment": {
          "risk_level": "low"
        }
      }
    ],
    "system_summary": {
      "most_critical_component": {
        "id": "component_005",
        "type": "reducer",
        "max_erosion_rate": {
          "value": 0.00108,
          "unit": "mm/year"
        }
      },
      "total_sand_consumption": {
        "value": 24.0,
        "unit": "tons/year"
      },
      "overall_risk_assessment": {
        "system_risk_level": "low",
        "erosion_class": 3,
        "recommendations": [
          "System operates within acceptable erosion limits",
          "Monitor reducer (component_005) more frequently",
          "Consider geometry factor validation for complex piping"
        ]
      },
      "next_inspection_recommendations": {
        "component_005": "2 years",
        "component_001": "5 years",
        "other_components": "Standard inspection cycle"
      }
    },
    "validation_results": {
      "input_validation": {
        "parameter_ranges": "all_within_limits",
        "model_applicability": "all_models_applicable",
        "warnings": []
      },
      "calculation_validation": {
        "mass_balance": "passed",
        "dimensional_analysis": "passed",
        "convergence": "achieved"
      }
    }
  }
}
